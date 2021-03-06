import os
import subprocess

def get_docker(ctx):
  ctx.logger.info("getting docker")
  ret=subprocess.call("wget -qO- https://get.docker.com/ | sed 's/docker-engine/docker-engine-1.11.2-0~trusty/' >/tmp/get_docker.sh",shell=True)
  ctx.logger.info("getting docker ret={}".format(ret))
  subprocess.call("sudo sh /tmp/get_docker.sh > /tmp/get_docker.out",shell=True)

def edit_docker_config(flannel):
  # edit docker config
  with open("/tmp/docker","w") as fd:
    with open("/etc/default/docker","r") as fdin:
      for line in fdin:
        fd.write(line)
  with open("/tmp/docker","a") as fd:
    fd.write(flannel+"\n")
    fd.write('DOCKER_OPTS="--bip=${FLANNEL_SUBNET} --mtu=${FLANNEL_MTU}"\n')

  subprocess.call("sudo mv /tmp/docker /etc/default/docker",shell=True)

