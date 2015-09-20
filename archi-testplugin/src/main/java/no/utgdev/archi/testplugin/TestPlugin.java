package no.utgdev.archi.testplugin;

import net.xeoh.plugins.base.annotations.PluginImplementation;
import no.utgdev.archi.api.PluginAPI;

@PluginImplementation
public class TestPlugin implements PluginAPI {

    public String hello() {
        return "From classpath plugin2";
    }

}
