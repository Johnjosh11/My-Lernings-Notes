#!/bin/sh
cd /home/user/Downloads/resin-3.1.15/bin
./httpd.sh -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=9080 stop
rm -rf prepaid.* pgw.*
echo resin stopped and removed prepaid and pgw files
echo Build all upstream 
cd /home/user/git/devel/software/prepaid
iant clean build-all-upstream publish
echo build all upstream completed

iant -Dinstall-spec-file=web-localhost1 clean-app generate-war
echo generated web war
iant -Dinstall-spec-file=pgw-localhost1 clean-app generate-war
echo generated gpw war
cd /home/user/Downloads/resin-3.1.15/webapps
ln -s /home/user/git/devel/software/prepaid/build/prepaid1-1.0-SNAPSHOT.war prepaid.war
ln -s /home/user/git/devel/software/prepaid/build/pgw1-1.0-SNAPSHOT.war pgw.war
echo placed war files at resin webapps folder
cd /home/user/Downloads/resin-3.1.15/bin
./httpd.sh -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=9080 start
echo started resin