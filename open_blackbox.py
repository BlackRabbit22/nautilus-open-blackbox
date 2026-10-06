import subprocess
import urllib.parse

from gi.repository import Nautilus, GObject

BLACKBOX = "com.raggesilver.BlackBox"


class OpenBlackBox(GObject.GObject, Nautilus.MenuProvider):
    """Adds "Open in Black Box" to the Nautilus folder context menu."""

    # The folder the user has selected right now (None if nothing is selected).
    _selected = None

    def get_file_items(self, files):
        """
        Nautilus tells us about the selection every time it changes,
        so save it here. The background handler can't see the selection,
        but it can read what we saved.
        """
        folders = [f for f in files if f.is_directory()]
        self._selected = folders[0] if folders else None
        if not folders:
            return []
        return self._item(folders[0])

    def get_background_items(self, current_folder):
        """
        Right-clicking empty space doesn't say what's selected,
        so open in the selected folder if there is one,
        otherwise just open in the folder we're looking at.
        """
        return self._item(self._selected or current_folder)

    def _item(self, folder):
        item = Nautilus.MenuItem(
            name="OpenBlackBox::open_here",
            label="Open in Black Box",
        )
        item.connect("activate", self._activate, folder)
        return [item]

    def _activate(self, menu, folder):
        # Cut off the "file://" part: "file:///home/me/dir" -> "/home/me/dir"
        path = urllib.parse.unquote(folder.get_uri()[7:])
        subprocess.Popen(
            ["flatpak", "run", BLACKBOX, "--working-directory=" + path]
        )
