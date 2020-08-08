from user_agents import parse
from urllib.parse import urlparse
from config.celery import app
from celery.utils.log import get_task_logger

from redirects_analyzer.models import RedirectData


logger = get_task_logger(__name__)


@app.task
def store_redirect_data(redirect_to='', referrer='', ip='', agent=''):
    user_agent = parse(agent)
    redirect_domain = urlparse(redirect_to)
    parsed_referrer = urlparse(referrer)
    referrer_domain = parsed_referrer.netloc

    RedirectData.objects.create(
        redirect_domain=redirect_domain.netloc,
        redirect_url=redirect_to.split('?')[0],
        redirect_params=redirect_domain.query,
        referrer_domain=referrer_domain,
        referrer_url=referrer,
        ip=ip,
        browser="{} {}".format(user_agent.browser.family, user_agent.browser.version_string),
        os="{} {}".format(user_agent.os.family, user_agent.os.version_string),
        platform=user_agent.device.family,
    )
    logger.info("saving redirect data done.")
