from celery import Celery, signature


def main():
    app = Celery()
    app.config_from_object(
        obj="celery-playground.celeryconfig",
        silent=False,
        force=True,
    )

    files = ["dir1", "dir2"]
    # Create the task signature using string references
    result = signature("celery-playground.workflow.tasks.start_workflow").apply_async(
        args=(files,)
    )
    print(result.get())


if __name__ == "__main__":
    main()
