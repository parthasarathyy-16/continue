from textwrap import dedent
from ..core.main import Step
from ..core.sdk import ContinueSDK
import os


class OpenConfigStep(Step):
    name: str = "Open config"

    async def describe(self, models):
        return dedent("""\
            `\"config.json\"` is now open. You can add a custom slash command in the `\"custom_commands\"` section, like in this example:
            ```json
            "custom_commands": [
                {
                    "name": "test",
                    "description": "Write unit tests like I do for the highlighted code"
                    "prompt": "Write a comprehensive set of unit tests for the selected code. It should setup, run tests that check for correctness including important edge cases, and teardown. Ensure that the tests are complete and sophisticated."
                }
            ],
            ```""")

    async def run(self, sdk: ContinueSDK):
        global_dir = os.path.expanduser('~/.continue')
        config_path = os.path.join(global_dir, 'config.json')
        await sdk.ide.setFileOpen(config_path)
