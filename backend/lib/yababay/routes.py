import json
from .queries import ethnical_by_source
from aiohttp.web import RouteTableDef, Response

routes = RouteTableDef()

@routes.get('/api/ethnical/{source_id}')
async def _ethnical_by_source(request):
    source_id = request.match_info['source_id']
    reply = ethnical_by_source(source_id)
    return Response(text=json.dumps(reply, ensure_ascii=False), content_type='application/json')

