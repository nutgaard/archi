package no.utgdev.archi.core;

import net.xeoh.plugins.base.PluginManager;
import net.xeoh.plugins.base.impl.PluginManagerFactory;
import net.xeoh.plugins.base.impl.PluginManagerImpl;
import net.xeoh.plugins.base.options.addpluginsfrom.OptionReportAfter;
import no.utgdev.archi.api.PluginAPI;

import java.net.URI;
import java.net.URISyntaxException;

public class Application {
    public static void main(String[] args) throws URISyntaxException {
        start();
    }

    public static void start() throws URISyntaxException {
        PluginManager pm = PluginManagerFactory.createPluginManager();

        pm.addPluginsFrom(new URI("http://localhost:8000/archi-testplugin-1.0-SNAPSHOT.jar"), new OptionReportAfter());
        System.out.println(((PluginManagerImpl) pm).getPluginRegistry().getAllPlugins());

        PluginAPI api = pm.getPlugin(PluginAPI.class);
        System.out.println();
        System.out.println(api.hello());
    }
}
