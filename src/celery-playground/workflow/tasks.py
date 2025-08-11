from pathlib import Path
import logging

from celery import shared_task, group, chord, chain

logger = logging.getLogger(__name__)


@shared_task
def extract_specific_files(dirs: tuple[str, ...]) -> tuple[str, ...]:
    evtx_files: tuple[str, ...] = tuple(
        str(Path("specific_files") / Path(d).name / "file.ext") for d in dirs
    )
    logger.info(f"Extracted files: {evtx_files} from directories: {dirs}")
    return evtx_files


@shared_task
def convert_files_to_csv(
    files: tuple[str, ...],
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    csv_files: tuple[str, ...] = tuple(str(Path(f).with_suffix(".csv")) for f in files)
    files_to_delete: tuple[str, ...] = files
    logger.info(f"Converted files: {files} to CSV: {csv_files}")
    return files_to_delete, csv_files


@shared_task
def delete_files(files: tuple[str, ...]) -> None:
    for file in files:
        logger.info(f"Deleting file: {file}")
    logger.info(f"Deleted {len(files)} files")


@shared_task
def send_files_to_api(files: tuple[str, ...]) -> None:
    for file in files:
        logger.info(f"Sending file to an API: {file}")
    logger.info(f"Sent {len(files)} files to the API")


@shared_task
def on_workflow_completed(results: tuple[str, ...]) -> None:
    logger.info(f"Workflow completed! Results: {results}")


@shared_task
def launch_parallel_and_callback(
    result: tuple[tuple[str, ...], tuple[str, ...]],
) -> None:
    files_to_delete, csv_files = result
    a_group: group = group(
        delete_files.s(files_to_delete), send_files_to_api.s(csv_files)
    )
    a_chord = chord(header=a_group, body=on_workflow_completed.s())
    a_chord.apply_async()


@shared_task
def start_workflow(files) -> None:
    sequential_chain = chain(extract_specific_files.s(files) | convert_files_to_csv.s())
    full_chain = chain(sequential_chain | launch_parallel_and_callback.s())
    full_chain.apply_async()
