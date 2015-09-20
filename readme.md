# Preinstall
jspf is not in the maven repository, thus you need to install them locally.

```
cd maven
mvn install:install-file -Dfile=jspf.core-1.0.3.jar -DgroupId=net.xeon -DartifactId=jspf.core -Dversion=1.0.3 -Dpackaging=jar -DgeneratePom=true
mvn install:install-file -Dfile=jspf.core-1.0.3-sources.jar -DgroupId=net.xeon -DartifactId=jspf.core -Dversion=1.0.3 -Dpackaging=jar -Dclassifier=sources -DgeneratePom=true
mvn install:install-file -Dfile=jspf.core-1.0.3-javadoc.jar -DgroupId=net.xeon -DartifactId=jspf.core -Dversion=1.0.3 -Dpackaging=jar -Dclassifier=javadoc -DgeneratePom=true
```
