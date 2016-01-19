

### test if the match url is integer
def integers(*segment_names):
    def predicate(info, request):
        match = info['match']
        for segment_name in segment_names:
            try:
                print (segment_names)
                match[segment_name] = int(match[segment_name])
                if int(match[segment_name]) == 0 :
                    print(' ****** ACTIONS FORMS ******')
                    return False
            except (TypeError, ValueError):
                return False
        return True
    return predicate

def add_routes(config):
    ##### Security routes #####
    config.add_route('security/login', 'portal-core/security/login')
    config.add_route('security/logout', 'portal-core/security/logout')
    config.add_route('security/has_access', 'portal-core/security/has_access')

    ##### User #####
    config.add_route('core/user', 'portal-core/user')
    config.add_route('core/currentUser', 'portal-core/currentUser')


    ##### Site #####
    config.add_route('core/site', 'portal-core/site')
    config.add_route('core/instance', 'portal-core/instance')






