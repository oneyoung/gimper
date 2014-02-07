from gimpfu import *


def plugin_main():
    pass


register(
    "python_jpg_saver",
    "Save current image, resize and export to jpeg format.",
    "Resize current image first, then export to jpeg format, save and close current image.",
    "oneyoung",
    "Copyright 2014 oneyoung",
    "2014",
    N_("Save to jpeg"),  # menu item
    "",  # image type
    [],  # parameters
    [],  # return value
    plugin_main,
    menu=N_("<Image>/File"),  # menupath
    domain=("gimp20-python", gimp.locale_directory)
)

main()
