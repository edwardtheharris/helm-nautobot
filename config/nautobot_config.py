"""Nautobot configuration settings."""
import os
import re
import tempfile

from loguru import logger

from nautobot.core.settings import ALLOWED_URL_SCHEMES
from nautobot.core.settings import AUTHENTICATION_BACKENDS
from nautobot.core.settings import CACHES
# from nautobot.core.settings import CACHEOPS_DEFAULTS
# from nautobot.core.settings import CACHEOPS_ENABLED
from nautobot.core.settings import CELERY_BROKER_URL
# from nautobot.core.settings import CELERY_BEAT_HEARTBEAT_FILE
from nautobot.core.settings import CELERY_TASK_DEFAULT_QUEUE
from nautobot.core.settings import DATABASES
from nautobot.core.settings import INSTALLED_APPS
from nautobot.core.settings import JOBS_ROOT
from nautobot.core.settings import MAINTENANCE_MODE
from nautobot.core.settings import METRICS_ENABLED
from nautobot.core.settings import MIDDLEWARE
from nautobot.core.settings import NAUTOBOT_ROOT
from nautobot.core.settings import PLUGINS
from nautobot.core.settings import ROOT_URLCONF
# from nautobot.core.settings import RQ_QUEUES
from nautobot.core.settings import SANITIZER_PATTERNS
from nautobot.core.settings import SECRET_KEY
from nautobot.core.settings import STATIC_ROOT
from nautobot.core.settings import STATIC_URL
from nautobot.core.settings import STORAGE_BACKEND
from nautobot.core.settings import STORAGE_CONFIG
from nautobot.core.settings import TEMPLATES
from nautobot.core.settings_funcs import is_truthy
from nautobot.core.settings_funcs import parse_redis_connection

#########################
#                       #
#   Required settings   #
#                       #
#########################

logger.debug(f'cache ops defaults: {MIDDLEWARE}')
# logger.debug(f'cache ops defaults: {CACHEOPS_DEFAULTS}')
# logger.debug(f'cache ops enabled: {CACHEOPS_ENABLED}')
logger.debug(f'celery task default queue: {CELERY_TASK_DEFAULT_QUEUE}')
logger.debug(f'installed apps: {INSTALLED_APPS}')
# logger.debug(f'rq queues: {RQ_QUEUES}')
logger.debug(f'secret key: {SECRET_KEY}')
# This is a list of valid fully-qualified domain names (FQDNs) for the Nautobot
# server. Nautobot will not permit write
# access to the server via any other hostnames. The first FQDN in the list will
# be treated as the preferred name.
#
# Example: ALLOWED_HOSTS = ['nautobot.example.com', 'nautobot.internal.local']
#
ALLOWED_HOSTS = os.getenv("NAUTOBOT_ALLOWED_HOSTS", "").split(" ")


# logger.debug(AUTHENTICATION_BACKENDS)
logger.debug(JOBS_ROOT)
logger.debug(MAINTENANCE_MODE)
logger.debug(METRICS_ENABLED)
logger.debug(PLUGINS)
logger.debug(SANITIZER_PATTERNS)
logger.debug(STATIC_ROOT)
logger.debug(STORAGE_BACKEND)
logger.debug(STORAGE_CONFIG)

AUTH_USER_MODEL = "users.User"
AUTHENTICATION_BACKENDS = [
    # 'social_core.backends.github.GithubOAuth2',
    # 'django.contrib.auth.backends.ModelBackend',
    'nautobot.core.authentication.ObjectPermissionBackend',
]
logger.debug(f'authentication backends: {AUTHENTICATION_BACKENDS}')

# The django-redis cache is used to establish concurrent locks using Redis.
#
# "django_prometheus.cache.backends.redis.RedisCache"
# if METRICS_ENABLED else "django_redis.cache.RedisCache",
CACHES = {
    "default": {
        "BACKEND": os.getenv(
            "NAUTOBOT_CACHES_BACKEND",
            'django_redis.cache.RedisCache'
        ),
        "LOCATION": parse_redis_connection(redis_database=1),
        "TIMEOUT": 300,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",
        },
    }
}

logger.debug(f'caches: {CACHES}')
logger.debug(f'root url conf: {ROOT_URLCONF}')
# Number of seconds to cache ContentType lookups. Set to 0 to disable caching.
# CONTENT_TYPE_CACHE_TIMEOUT = int(os.getenv("NAUTOBOT_CONTENT_TYPE_CACHE_TIMEOUT", "0"))

# Celery Beat heartbeat file path - will be touched by Beat each time it wakes
# up as a proof-of-health.
CELERY_BEAT_HEARTBEAT_FILE = os.getenv(
    "NAUTOBOT_CELERY_BEAT_HEARTBEAT_FILE",
    os.path.join(tempfile.gettempdir(), "nautobot_celery_beat_heartbeat"),
)

# Celery broker URL used to tell workers where queues are located
#
CELERY_BROKER_URL = os.getenv(
    "NAUTOBOT_CELERY_BROKER_URL", parse_redis_connection(redis_database=0))
logger.debug(f'celery broker url: {CELERY_BROKER_URL}')

# Optional configuration dict for Celery to use custom SSL certificates to connect to Redis.
#
# CELERY_BROKER_USE_SSL = None

# Database configuration. See the Django documentation for a complete list of available parameters:
#   https://docs.djangoproject.com/en/stable/ref/settings/#databases
#
DATABASES = {
    "default": {
        "NAME": os.getenv("NAUTOBOT_DB_NAME", "nautobot"),  # Database name
        "USER": os.getenv("NAUTOBOT_DB_USER", ""),  # Database username
        "PASSWORD": os.getenv("NAUTOBOT_DB_PASSWORD", ""),  # Database password
        "HOST": os.getenv("NAUTOBOT_DB_HOST", "localhost"),  # Database server
        "PORT": os.getenv("NAUTOBOT_DB_PORT", ""),  # Database port (leave blank for default)
        "CONN_MAX_AGE": int(os.getenv("NAUTOBOT_DB_TIMEOUT", "300")),  # Database timeout
        "ENGINE": os.getenv(
            "NAUTOBOT_DB_ENGINE",
            'django.db.backends.postgresql',
        ),  # Database driver ("mysql" or "postgresql")
    }
}

# Ensure proper Unicode handling for MySQL
#
if DATABASES["default"]["ENGINE"].endswith("mysql"):
    DATABASES["default"]["OPTIONS"] = {"charset": "utf8mb4"}

# This key is used for secure generation of random numbers and strings.
# It must never be exposed outside of this file.
# For optimal security, SECRET_KEY should be at least 50 characters
# in length and contain a mix of letters, numbers, and
# symbols. Nautobot will not run without this defined. For more information, see
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = os.getenv(
    'NAUTOBOT_SECRET_KEY',
    r'57evlrs^0pmu5#ys=9t6==lf6hdz&amp;$1)qq-(%f1noo_b+nsy@f')

#####################################
#                                   #
#   Optional Django core settings   #
#                                   #
#####################################

# Specify one or more (name, email address) tuples representing Nautobot
# administrators.
# These people will be notified of application errors (assuming correct email
# settings are provided).
#
# ADMINS = []

# FQDNs that are considered trusted origins for secure, cross-domain, requests
# such as HTTPS POST.
# If running Nautobot under a single domain, you may not need to set this
# variable;
# if running on multiple domains, you *may* need to set this variable to more
# or less the same as ALLOWED_HOSTS above.
# https://docs.djangoproject.com/en/stable/ref/settings/#csrf-trusted-origins
#
# CSRF_TRUSTED_ORIGINS = []

# Date/time formatting. See the following link for supported formats:
# https://docs.djangoproject.com/en/stable/ref/templates/builtins/#date
#
DATE_FORMAT = os.getenv("NAUTOBOT_DATE_FORMAT", "N j, Y")
SHORT_DATE_FORMAT = os.getenv("NAUTOBOT_SHORT_DATE_FORMAT", "Y-m-d")
TIME_FORMAT = os.getenv("NAUTOBOT_TIME_FORMAT", "g:i a")
DATETIME_FORMAT = os.getenv("NAUTOBOT_DATETIME_FORMAT", "N j, Y g:i a")
SHORT_DATETIME_FORMAT = os.getenv("NAUTOBOT_SHORT_DATETIME_FORMAT", "Y-m-d H:i")

logger.debug(f'templates: {TEMPLATES}')
# MIDDLEWARE.append('django.contrib.sessions.middleware.SessionMiddleware')
# MIDDLEWARE.append('django.contrib.auth.middleware.AuthenticationMiddleware')
# MIDDLEWARE.append('django.contrib.messages.middleware.MessageMiddleware')


# Set to True to enable server debugging. WARNING: Debugging introduces a
# substantial performance penalty and may reveal
# sensitive information about your installation. Only enable debugging while
# performing testing. Never enable debugging
# on a production system.
#
DEBUG = is_truthy(os.getenv("NAUTOBOT_DEBUG", "False"))

# If hosting Nautobot in a subdirectory, you must set this value to match the
# base URL prefix configured in your
# HTTP server (e.g. `/nautobot/`). When not set, URLs will default to
# being prefixed by `/`.
#
# FORCE_SCRIPT_NAME = None

# IP addresses recognized as internal to the system.
#
INTERNAL_IPS = ("127.0.0.1", "::1")

# Enable custom logging. Please see the Django documentation for detailed
# guidance on configuring custom logs:
#   https://docs.djangoproject.com/en/stable/topics/logging/
#
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "normal": {
            "format": (
                "%(asctime)s.%(msecs)03d %(levelname)-7s %(name)s :\n  %(message)s"
                ),
            "datefmt": "%H:%M:%S",
        },
        "verbose": {
            "format": (
                '%(asctime)s.%(msecs)03d %(levelname)-7s %(name)-20s '
                '%(filename)-15s %(funcName)30s() :\n  %(message)s'
            ),
            "datefmt": "%H:%M:%S",
        },
    },
    "handlers": {
        "normal_console": {
            "level": "INFO",
            "class": 'logging.StreamHandler',
            "formatter": "normal",
        },
        "verbose_console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {"handlers": ["normal_console"], "level": "INFO"},
        "nautobot": {
            "handlers": ["verbose_console" if DEBUG else "normal_console"],
            "level": "DEBUG" if DEBUG else "INFO",
        },
    },
}

# The file path where uploaded media such as image attachments are stored.
# A trailing slash is not needed.
#
MEDIA_ROOT = os.path.join(NAUTOBOT_ROOT, "media").rstrip("/")

# Set to True to use session cookies instead of persistent cookies.
# Session cookies will expire when a browser is closed.
#
SESSION_EXPIRE_AT_BROWSER_CLOSE = is_truthy(
    os.getenv("NAUTOBOT_SESSION_EXPIRE_AT_BROWSER_CLOSE", "False"))

# The length of time (in seconds) for which a user will remain logged into
# the web UI before being prompted to
# re-authenticate. (Default: 1209600 [14 days])
#
SESSION_COOKIE_AGE = int(
    os.getenv("NAUTOBOT_SESSION_COOKIE_AGE", "1209600"))  # 2 weeks, in seconds

# Where Nautobot stores user session data.
#
SESSION_ENGINE = "django.contrib.sessions.backends.db"

# By default, Nautobot will store session data in the database. Alternatively,
# a file path can be specified here to use
# local file storage instead. (This can be useful for enabling authentication
# on a standby instance with read-only
# database access.) Note that the user as which Nautobot runs must have read
# and write permissions to this path.
#
# SESSION_FILE_PATH = os.getenv("NAUTOBOT_SESSION_FILE_PATH", None)

# Where static files (CSS, JavaScript, etc.) are stored
#
STATIC_ROOT = os.path.join(NAUTOBOT_ROOT, "static")
STATIC_URL = 'static/'
logger.debug(f'static url {STATIC_URL}')

# Time zone (default: UTC)
#
# TIME_ZONE = os.getenv("NAUTOBOT_TIME_ZONE", "UTC")

###################################################################
#                                                                 #
#   Optional settings specific to Nautobot and its related apps   #
#                                                                 #
###################################################################

# Allow users to enable request profiling via django-silk for admins to inspect.
# if ("NAUTOBOT_ALLOW_REQUEST_PROFILING" in os.environ
#       and os.environ["NAUTOBOT_ALLOW_REQUEST_PROFILING"] != ""):
#     ALLOW_REQUEST_PROFILING = is_truthy(os.environ["NAUTOBOT_ALLOW_REQUEST_PROFILING"])

# URL schemes that are allowed within links in Nautobot
#
ALLOWED_URL_SCHEMES = (
    "file",
    "ftp",
    "ftps",
    "http",
    "https",
    "irc",
    "mailto",
    "sftp",
    "ssh",
    "tel",
    "telnet",
    "tftp",
    "vnc",
    "xmpp",
)
logger.debug(f'allowed url schemes: {ALLOWED_URL_SCHEMES}')

# Banners (HTML is permitted) to display at the top and/or bottom of all
# Nautobot pages, and on the login page itself.
#
# if "NAUTOBOT_BANNER_BOTTOM" in os.environ and os.environ["NAUTOBOT_BANNER_BOTTOM"] != "":
#     BANNER_BOTTOM = os.environ["NAUTOBOT_BANNER_BOTTOM"]
# if "NAUTOBOT_BANNER_LOGIN" in os.environ and os.environ["NAUTOBOT_BANNER_LOGIN"] != "":
#     BANNER_LOGIN = os.environ["NAUTOBOT_BANNER_LOGIN"]
# if "NAUTOBOT_BANNER_TOP" in os.environ and os.environ["NAUTOBOT_BANNER_TOP"] != "":
#     BANNER_TOP = os.environ["NAUTOBOT_BANNER_TOP"]

# Branding logo locations. The logo takes the place of the Nautobot logo in the
# top right of the nav bar.
# The filepath should be relative to the `MEDIA_ROOT`.
#
# BRANDING_FILEPATHS = {
#     "logo": os.getenv("NAUTOBOT_BRANDING_FILEPATHS_LOGO", None),  # Navbar logo
#     "favicon": os.getenv("NAUTOBOT_BRANDING_FILEPATHS_FAVICON", None),  # Browser favicon
#     "icon_16": os.getenv("NAUTOBOT_BRANDING_FILEPATHS_ICON_16", None),  # 16x16px icon
#     "icon_32": os.getenv("NAUTOBOT_BRANDING_FILEPATHS_ICON_32", None),  # 32x32px icon
#     "icon_180": os.getenv(
#         "NAUTOBOT_BRANDING_FILEPATHS_ICON_180", None
#     ),  # 180x180px icon - used for the apple-touch-icon header
#     "icon_192": os.getenv("NAUTOBOT_BRANDING_FILEPATHS_ICON_192", None),  # 192x192px icon
#     "icon_mask": os.getenv(
#         "NAUTOBOT_BRANDING_FILEPATHS_ICON_MASK", None
#     ),  # mono-chrome icon used for the mask-icon header
#     "header_bullet": os.getenv(
#         "NAUTOBOT_BRANDING_FILEPATHS_HEADER_BULLET", None
#     ),  # bullet image used for various view headers
#     "nav_bullet": os.getenv("NAUTOBOT_BRANDING_FILEPATHS_NAV_BULLET", None),
# # bullet image used for nav menu headers
#     "css": os.getenv("NAUTOBOT_BRANDING_FILEPATHS_CSS", None),  # Custom global CSS
#     "javascript": os.getenv("NAUTOBOT_BRANDING_FILEPATHS_JAVASCRIPT", None),
# # Custom global JavaScript
# }

# Prepended to CSV, YAML and export template filenames (i.e. `nautobot_device.yml`)
#
# BRANDING_PREPENDED_FILENAME = os.getenv("NAUTOBOT_BRANDING_PREPENDED_FILENAME", "nautobot_")

# Title to use in place of "Nautobot"
#
# BRANDING_TITLE = os.getenv("NAUTOBOT_BRANDING_TITLE", "Nautobot")

# Branding URLs (links in the bottom right of the footer)
#
# BRANDING_URLS = {
#     "code": os.getenv("NAUTOBOT_BRANDING_URLS_CODE", "https://github.com/nautobot/nautobot"),
#     "docs": os.getenv("NAUTOBOT_BRANDING_URLS_DOCS", None),
#     "help": os.getenv("NAUTOBOT_BRANDING_URLS_HELP", "https://github.com/nautobot/nautobot/wiki"),
# }

# Options to pass to the Celery broker transport, for example when using Celery with Redis Sentinel.
#
# CELERY_BROKER_TRANSPORT_OPTIONS = {}

# Default celery queue name that will be used by workers and tasks if no queue is specified
# CELERY_TASK_DEFAULT_QUEUE = os.getenv("NAUTOBOT_CELERY_TASK_DEFAULT_QUEUE", "default")

# Global task time limits (seconds)
# Exceeding the soft limit will result in a SoftTimeLimitExceeded exception,
# while exceeding the hard limit will result in a SIGKILL.
#
# CELERY_TASK_SOFT_TIME_LIMIT = int(os.getenv("NAUTOBOT_CELERY_TASK_SOFT_TIME_LIMIT", str(5 * 60)))
# CELERY_TASK_TIME_LIMIT = int(os.getenv("NAUTOBOT_CELERY_TASK_TIME_LIMIT", str(10 * 60)))

# Ports for prometheus metric HTTP server running on the celery worker.
# Normally this should be set to a single port, unless you have multiple
# workers running on a single machine, i.e.
# sharing the same available ports. In that case you need to specify a range
# of ports greater than or equal to the
# highest amount of workers you are running on a single machine
# (comma-separated, like "8080,8081,8082"). You can then
# use the `target_limit` parameter to the Prometheus `scrape_config` to ensure
# you are not getting duplicate metrics in
# that case. Set this to an empty string to disable it.
CELERY_WORKER_PROMETHEUS_PORTS = []
# if os.getenv("NAUTOBOT_CELERY_WORKER_PROMETHEUS_PORTS"):
#     CELERY_WORKER_PROMETHEUS_PORTS = [
#         int(value) for value in os.getenv("NAUTOBOT_CELERY_WORKER_PROMETHEUS_PORTS").split(",")
#     ]


# Number of days to retain changelog entries. Set to 0 to retain changes
# indefinitely. Defaults to 90 if not set here.
#
# if ("NAUTOBOT_CHANGELOG_RETENTION" in os.environ
#         and os.environ["NAUTOBOT_CHANGELOG_RETENTION"] != ""):
#     CHANGELOG_RETENTION = int(os.environ["NAUTOBOT_CHANGELOG_RETENTION"])

# If True, all origins will be allowed. Other settings restricting allowed origins will be ignored.
# Defaults to False. Setting this to True can be dangerous, as it allows any website to make
# cross-origin requests to yours. Generally you'll want to restrict the list of allowed origins with
# CORS_ALLOWED_ORIGINS or CORS_ALLOWED_ORIGIN_REGEXES.
#
CORS_ALLOW_ALL_ORIGINS = is_truthy(os.getenv("NAUTOBOT_CORS_ALLOW_ALL_ORIGINS", "False"))

# A list of origins that are authorized to make cross-site HTTP requests. Defaults to [].
#
# CORS_ALLOWED_ORIGINS = [
#     'https://hostname.example.com',
# ]

# A list of strings representing regexes that match Origins that are authorized to make cross-site
# HTTP requests. Defaults to [].
#
# CORS_ALLOWED_ORIGIN_REGEXES = [
#     r'^(https?://)?(\w+\.)?example\.com$',
# ]

# UUID uniquely but anonymously identifying this Nautobot deployment.
#
# if "NAUTOBOT_DEPLOYMENT_ID" in os.environ and os.environ["NAUTOBOT_DEPLOYMENT_ID"] != "":
#     DEPLOYMENT_ID = os.environ["NAUTOBOT_DEPLOYMENT_ID"]

# Device names are not guaranteed globally-unique by Nautobot but in practice they often are.
# Set this to True to use the device name alone as the natural key for Device objects.
# Set this to False to use the sequence (name, tenant, location) as the natural key instead.
#
# if "NAUTOBOT_DEVICE_NAME_AS_NATURAL_KEY" in os.environ and
#       os.environ["NAUTOBOT_DEVICE_NAME_AS_NATURAL_KEY"] != "":
#     DEVICE_NAME_AS_NATURAL_KEY = is_truthy(os.environ["NAUTOBOT_DEVICE_NAME_AS_NATURAL_KEY"])

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# The number of seconds to cache the member list of dynamic groups.
# Set this to `0` to disable caching.
#
# if (
#     "NAUTOBOT_DYNAMIC_GROUPS_MEMBER_CACHE_TIMEOUT" in os.environ
#     and os.environ["NAUTOBOT_DYNAMIC_GROUPS_MEMBER_CACHE_TIMEOUT"] != ""
# ):
#     DYNAMIC_GROUPS_MEMBER_CACHE_TIMEOUT = int(
    # os.environ["NAUTOBOT_DYNAMIC_GROUPS_MEMBER_CACHE_TIMEOUT"])

# Exempt certain models from the enforcement of view permissions. Models listed
# here will be viewable by all users and
# by anonymous users. List models in the form `<app>.<model>`.
# Add '*' to this list to exempt all models.
# Defaults to [].
#
# EXEMPT_VIEW_PERMISSIONS = [
#     'dcim.location',
#     'ipam.prefix',
# ]

# Global 3rd-party authentication settings
#
# EXTERNAL_AUTH_DEFAULT_GROUPS = []
# EXTERNAL_AUTH_DEFAULT_PERMISSIONS = {}

# Directory where cloned Git repositories will be stored.
#
GIT_ROOT = os.getenv("NAUTOBOT_GIT_ROOT", os.path.join(NAUTOBOT_ROOT, "git").rstrip("/"))

# Prefixes to use for custom fields, relationships, and computed
# fields in GraphQL representation of data.
#
# GRAPHQL_COMPUTED_FIELD_PREFIX = "cpf"
# GRAPHQL_CUSTOM_FIELD_PREFIX = "cf"
# GRAPHQL_RELATIONSHIP_PREFIX = "rel"

# HTTP proxies Nautobot should use when sending outbound HTTP requests (e.g. for webhooks).
#
# HTTP_PROXIES = {
#     'http': 'http://10.10.1.10:3128',
#     'https': 'http://10.10.1.10:1080',
# }

# Send anonymized installation metrics when `nautobot-server post_upgrade` command is run.
#
# INSTALLATION_METRICS_ENABLED = is_truthy(
    # os.getenv("NAUTOBOT_INSTALLATION_METRICS_ENABLED", "True"))

# Storage backend to use for Job input files and Job output files.
#
# Note: the default is for backwards compatibility and it is recommended to
# change it if possible for your deployment.
#
JOB_FILE_IO_STORAGE = os.getenv(
    "NAUTOBOT_JOB_FILE_IO_STORAGE", "db_file_storage.storage.DatabaseFileStorage")

# Maximum size in bytes of any single file created by Job.create_file().
#
# JOB_CREATE_FILE_MAX_SIZE = 10 << 20

# Directory where Jobs can be discovered.
#
JOBS_ROOT = os.getenv("NAUTOBOT_JOBS_ROOT", os.path.join(NAUTOBOT_ROOT, "jobs").rstrip("/"))

# Location names are not guaranteed globally-unique by Nautobot but in practice they often are.
# Set this to True to use the location name alone as the natural key for Location objects.
# Set this to False to use the sequence (name, parent__name, parent__parent__name, ...)
# as the natural key instead.
#
# if "NAUTOBOT_LOCATION_NAME_AS_NATURAL_KEY" in os.environ
#       and os.environ["NAUTOBOT_LOCATION_NAME_AS_NATURAL_KEY"] != "":
#     LOCATION_NAME_AS_NATURAL_KEY = is_truthy(os.environ["NAUTOBOT_LOCATION_NAME_AS_NATURAL_KEY"])

# Log Nautobot deprecation warnings. Note that this setting is ignored
# (deprecation logs always enabled) if DEBUG = True
#
# LOG_DEPRECATION_WARNINGS = is_truthy(os.getenv("NAUTOBOT_LOG_DEPRECATION_WARNINGS", "False"))

# Setting this to True will display a "maintenance mode" banner at the top of every page.
#
MAINTENANCE_MODE = is_truthy(os.getenv("NAUTOBOT_MAINTENANCE_MODE", "False"))

# Maximum number of objects that the UI and API will retrieve in a single request. Default is 1000
#
# if "NAUTOBOT_MAX_PAGE_SIZE" in os.environ and os.environ["NAUTOBOT_MAX_PAGE_SIZE"] != "":
#     MAX_PAGE_SIZE = int(os.environ["NAUTOBOT_MAX_PAGE_SIZE"])

# Expose Prometheus monitoring metrics at the HTTP endpoint '/metrics'
#
METRICS_ENABLED = is_truthy(os.getenv("NAUTOBOT_METRICS_ENABLED", "False"))

# Require API Authentication to HTTP endpoint '/metrics'
#
# METRICS_AUTHENTICATED = is_truthy(os.getenv("NAUTOBOT_METRICS_AUTHENTICATED", "False"))

# Disable app metrics for specific apps
#
# if "NAUTOBOT_METRICS_DISABLED_APPS" in os.environ
#       and os.environ["NAUTOBOT_METRICS_DISABLED_APPS"] != "":
#     METRICS_DISABLED_APPS = os.getenv("NAUTOBOT_METRICS_DISABLED_APPS", "").split(",")

# Credentials that Nautobot will uses to authenticate to devices when connecting via NAPALM.
#
# NAPALM_USERNAME = os.getenv("NAUTOBOT_NAPALM_USERNAME", "")
# NAPALM_PASSWORD = os.getenv("NAUTOBOT_NAPALM_PASSWORD", "")

# NAPALM timeout (in seconds). (Default: 30)
#
# NAPALM_TIMEOUT = int(os.getenv("NAUTOBOT_NAPALM_TIMEOUT", "30"))

# NAPALM optional arguments (see
# https://napalm.readthedocs.io/en/latest/support/#optional-arguments). Arguments must
# be provided as a dictionary.
#
# NAPALM_ARGS = {}

# Default number of objects to display per page of the UI and REST API. Default is 50
#
# if "NAUTOBOT_PAGINATE_COUNT" in os.environ and os.environ["NAUTOBOT_PAGINATE_COUNT"] != "":
#     PAGINATE_COUNT = int(os.environ["NAUTOBOT_PAGINATE_COUNT"])

# Options given in the web UI for the number of objects to display per page.
# Default is [25, 50, 100, 250, 500, 1000]
#
# if "NAUTOBOT_PER_PAGE_DEFAULTS" in os.environ and os.environ["NAUTOBOT_PER_PAGE_DEFAULTS"] != "":
#     PER_PAGE_DEFAULTS = [int(val) for val in os.environ["NAUTOBOT_PER_PAGE_DEFAULTS"].split(",")]

# Enable installed plugins. Add the name of each plugin to the list.
#
PLUGINS = []

# Plugins configuration settings. These settings are used by various
# plugins that the user may have installed.
# Each key in the dictionary is the name of an installed plugin and its value
# is a dictionary of settings.
#
# PLUGINS_CONFIG = {
#     'my_plugin': {
#         'foo': 'bar',
#         'buzz': 'bazz'
#     }
# }

# Prefer IPv6 addresses or IPv4 addresses in selecting a device's primary
# IP address? Default False
#
# if "NAUTOBOT_PREFER_IPV4" in os.environ and os.environ["NAUTOBOT_PREFER_IPV4"] != "":
#     PREFER_IPV4 = is_truthy(os.environ["NAUTOBOT_PREFER_IPV4"])

# Default height and width in pixels of a single rack unit in rendered rack
# elevations. Defaults are 22 and 230
#
# if (
#     "NAUTOBOT_RACK_ELEVATION_DEFAULT_UNIT_HEIGHT" in os.environ
#     and os.environ["NAUTOBOT_RACK_ELEVATION_DEFAULT_UNIT_HEIGHT"] != ""
# ):
#     RACK_ELEVATION_DEFAULT_UNIT_HEIGHT = int(
    # os.environ["NAUTOBOT_RACK_ELEVATION_DEFAULT_UNIT_HEIGHT"])
# if (
#     "NAUTOBOT_RACK_ELEVATION_DEFAULT_UNIT_WIDTH" in os.environ
#     and os.environ["NAUTOBOT_RACK_ELEVATION_DEFAULT_UNIT_WIDTH"] != ""
# ):
#     RACK_ELEVATION_DEFAULT_UNIT_WIDTH = int(
    # os.environ["NAUTOBOT_RACK_ELEVATION_DEFAULT_UNIT_WIDTH"])

# Enable two-digit format for the rack unit numbering in rack elevations.
#
# if (
#     "NAUTOBOT_RACK_ELEVATION_UNIT_TWO_DIGIT_FORMAT" in os.environ
#      and os.environ["NAUTOBOT_RACK_ELEVATION_UNIT_TWO_DIGIT_FORMAT"] != ""
# ):
#     RACK_ELEVATION_UNIT_TWO_DIGIT_FORMAT = is_truthy(
    # os.environ["NAUTOBOT_RACK_ELEVATION_UNIT_TWO_DIGIT_FORMAT"])

# Sets an age out timer of redis lock. This is NOT implicitly applied to locks, must be added
# to a lock creation as `timeout=settings.REDIS_LOCK_TIMEOUT`
#
REDIS_LOCK_TIMEOUT = int(os.getenv("NAUTOBOT_REDIS_LOCK_TIMEOUT", "600"))

# How frequently to check for a new Nautobot release on GitHub, and the URL
# to check for this information.
# Defaults to disabled (no URL) and check every 24 hours when enabled
#
# if "NAUTOBOT_RELEASE_CHECK_TIMEOUT" in os.environ
#          and os.environ["NAUTOBOT_RELEASE_CHECK_TIMEOUT"] != "":
#     RELEASE_CHECK_TIMEOUT = int(os.environ["NAUTOBOT_RELEASE_CHECK_TIMEOUT"])
# if "NAUTOBOT_RELEASE_CHECK_URL" in os.environ and os.environ["NAUTOBOT_RELEASE_CHECK_URL"] != "":
#     RELEASE_CHECK_URL = os.environ["NAUTOBOT_RELEASE_CHECK_URL"]

# Remote auth backend settings
#
REMOTE_AUTH_AUTO_CREATE_USER = True
REMOTE_AUTH_HEADER = "HTTP_REMOTE_USER"

logger.debug(f'{REMOTE_AUTH_AUTO_CREATE_USER}')
logger.debug(f'{REMOTE_AUTH_HEADER}')

# Job log entry sanitization and similar
#
SANITIZER_PATTERNS = [
    # General removal of username-like and password-like tokens
    (
        re.compile(
            r'(https?://)?\S+\s*@', re.IGNORECASE),
            r'\1{replacement}@'
        ),
    (
        re.compile(
            r'(username|password|passwd|pwd|secret|secrets)([\"\']?(?:\s+is.?|:)?\s+)\S+["\']?',
            re.IGNORECASE
        ),
        r'\1\2{replacement}',
    ),
]

# Configure SSO, for more information see docs/configuration/authentication/sso.md
#
SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_BACKEND_PREFIX = 'social_core.backends'
SOCIAL_AUTH_GITHUB_KEY = os.environ.get('SOCIAL_AUTH_GITHUB_KEY', '')
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get('SOCIAL_AUTH_GITHUB_SECRET', '')

# By default uploaded media is stored on the local filesystem. Using
# Django-storages is also supported. Provide the
# class path of the storage driver in STORAGE_BACKEND and any configuration
# options in STORAGE_CONFIG.
# These default to None and {} respectively.
#
# STORAGE_BACKEND = 'storages.backends.s3.S3Storage'
# STORAGE_CONFIG = {
#     'AWS_ACCESS_KEY_ID': 'Key ID',
#     'AWS_SECRET_ACCESS_KEY': 'Secret',
#     'AWS_STORAGE_BUCKET_NAME': 'nautobot',
#     'AWS_S3_REGION_NAME': 'eu-west-1',
# }

# Reject invalid UI/API filter parameters, or discard them while logging a warning?
#
# STRICT_FILTERING = is_truthy(os.getenv("NAUTOBOT_STRICT_FILTERING", "True"))

# Custom message to display on 4xx and 5xx error pages. Markdown and HTML are supported.
# Default message directs the user to #nautobot on NTC's Slack community.
#
# if "NAUTOBOT_SUPPORT_MESSAGE" in os.environ and os.environ["NAUTOBOT_SUPPORT_MESSAGE"] != "":
#     SUPPORT_MESSAGE = os.environ["NAUTOBOT_SUPPORT_MESSAGE"]

# UI_RACK_VIEW_TRUNCATE_FUNCTION
#
# def UI_RACK_VIEW_TRUNCATE_FUNCTION(device_display_name):
#     """Given device display name, truncate to fit the rack elevation view.
#
#     :param device_display_name: Full display name of the device attempting to
#           be rendered in the rack elevation.
#     :type device_display_name: str
#
#     :return: Truncated device name
#     :type: str
#     """
#     return str(device_display_name).split(".")[0]

# A list of strings designating all applications that are enabled in this Django installation.
# Each string should be a dotted Python path to an application configuration class (preferred),
# or a package containing an application.
# https://docs.nautobot.com/projects/core/en/latest/configuration/optional-settings/#extra-applications
# EXTRA_INSTALLED_APPS = [
#     'social_django',
# ]
# logger.debug(f'{EXTRA_INSTALLED_APPS}')
# INSTALLED_APPS.append(
#     'django.contrib.contenttypes',
# )

# Allow users to enable request profiling on their login session
ALLOW_REQUEST_PROFILING = False