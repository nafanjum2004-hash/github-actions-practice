from st2common.runners.base_action import BaseAction


class HelloAction(BaseAction):

    def run(self):
        return "Hello from GitHub Actions Demo Pack!"