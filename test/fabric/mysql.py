from fabric.api import env, run, task
from envassert import detect, file, group, package, port, process, service, \
    user
from hot.utils.test import get_artifacts, http_check


@task
def check():
    env.platform_family = detect.detect()

    assert package.installed("mysql-server-5.5")
    assert port.is_listening(3306)
    assert process.is_up("mysqld")
    assert file.exists("/root/.my.cnf")


@task
def holland():
    # Verify hollandbackup package is installed with a default backupset
    env.platform_family = detect.detect()

    assert package.installed("holland")
    assert package.installed("holland-mysqldump")
    assert file.exists("/etc/holland/backupsets/default.conf")


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
