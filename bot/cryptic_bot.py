from pathlib import Path

from PyDrocsid.config import Config, load_config_file, load_version
from PyDrocsid.environment import SENTRY_DSN
from PyDrocsid.logger import get_logger, setup_sentry


logger = get_logger(__name__)

logger.debug("loading config")
load_config_file(Path("config.yml"))

logger.debug("loading version")
load_version()

print(
    "\033[1m\033[36m"
    r"""

       ______                 __  _         ____        __
      / ____/______  ______  / /_(_)____   / __ )____  / /_
     / /   / ___/ / / / __ \/ __/ / ___/  / __  / __ \/ __/
    / /___/ /  / /_/ / /_/ / /_/ / /__   / /_/ / /_/ / /_
    \____/_/   \__, / .___/\__/_/\___/  /_____/\____/\__/
              /____/_/

    """
    "\033[0m"
)

logger.info(f"Starting {Config.NAME} v{Config.VERSION} ({Config.REPO_LINK})\n")

if SENTRY_DSN:
    logger.debug("initializing sentry")
    setup_sentry(SENTRY_DSN, Config.NAME, Config.VERSION)

from bot import run  # noqa: E402


run()
