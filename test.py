from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

# ctx = ClientContext('https://portal.kiewit.com/teams/bw20036202/constopr')
# ctx.with_user_credentials('jorge.carrillo1@kiewit.com', 'Anamaria.08Sarita.16')
# web = ctx.web.get().execute_query()
# print(web.url)

url = 'https://portal.kiewit.com/teams/bw20036202/constopr'
ctx_auth = AuthenticationContext(url)
if ctx_auth.acquire_token_for_user('jorge.carrillo1@kiewit.com', ''):
    ctx = ClientContext(url, ctx_auth)
    web = ctx.web
    ctx.load(web)
    ctx.execute_query()
    print("Web title: {0}".format(web.properties['Title']))
else:
    print(ctx_auth.get_last_error())