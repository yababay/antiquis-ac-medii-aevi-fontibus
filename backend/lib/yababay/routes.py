import json
from .queries import ethnical_count, ethnical_sents
from aiohttp.web import RouteTableDef, Response

routes = RouteTableDef()


@routes.get('/api/ethnical/sents/{source_id}/{ethnos}')
async def _ethnical_sents(request):
    source_id = request.match_info['source_id']
    ethnos = request.match_info['ethnos']
    reply = ethnical_sents(source_id, ethnos)
    return Response(text=json.dumps(reply, ensure_ascii=False), content_type='application/json')


@routes.get('/api/ethnical/count/{source_id}')
async def _ethnical_count(request):
    source_id = request.match_info['source_id']
    reply = ethnical_count(source_id)
    return Response(text=json.dumps(reply, ensure_ascii=False), content_type='application/json')

