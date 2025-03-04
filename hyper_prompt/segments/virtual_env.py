import os

from ..segment import BasicSegment


class Segment(BasicSegment):
    SYMBOL = "\uf820"

    def activate(self):
        env = (
            self.getenv("VIRTUAL_ENV")
            or self.getenv("CONDA_ENV_PATH")
            or self.getenv("CONDA_DEFAULT_ENV")
        )
        if self.getenv("VIRTUAL_ENV") and os.path.basename(env) == ".venv":
            env = os.path.basename(os.path.dirname(env))
        if not env:
            return
        env_name = os.path.basename(env)
        content = self.symbol("venv") + env_name

        bg = self.theme.get("VIRTUAL_ENV_BG", 35)
        fg = self.theme.get("VIRTUAL_ENV_FG", 00)
        self.append(self.hyper_prompt._content % (content), fg, bg)
