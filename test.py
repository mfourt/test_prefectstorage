import prefect
from prefect import task, Flow
from prefect.storage import Git

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")

with Flow("hello-flow") as flow:
    hello_task()

flow = Flow("hello-flow")
flow.storage = Git(repo="mfourt/test_prefectstorage", flow_path="/test.py", repo_host="github.com")
