from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        "FEATURES['SHOW_HEADER_LANGUAGE_SELECTOR'] = True"
    )
)
