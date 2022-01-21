from aiohttp.web import RouteTableDef, Response

routes = RouteTableDef()


@routes.get('/api/hello/world')
async def hello_world(_):
    return Response(text="Привет, мир!")

