def call(version=None, fix_with_iview=False):
    from uliweb import settings
    version = version or settings.UI_VERSION.get("ui.bootstrap3")
    a = [
        'modules/bootstrap/{version}/css/bootstrap.min.css'.format(version=version),
        '<!--[if lt IE 9]>/static/modules/bootstrap/asset/html5shiv.min.js<![endif]-->',
        '<!--[if lt IE 9]>/static/modules/bootstrap/asset/respond.min.js<![endif]-->',
        'modules/bootstrap/{version}/js/bootstrap.min.js'.format(version=version)
    ]

    if fix_with_iview:
        a.append("modules/bootstrap/fixwithiview.css")
    return {'toplinks': a}
