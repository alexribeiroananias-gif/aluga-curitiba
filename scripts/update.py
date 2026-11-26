import json, os, urllib.request, datetime, pathlib, math
root=pathlib.Path(__file__).resolve().parents[1]
urls=json.loads(os.environ.get('FEED_URLS','[]'))
if not urls: raise SystemExit('Configure FEED_URLS com feeds JSON autorizados.')
items={}
for url in urls:
    if not url.startswith('https://'): raise ValueError('HTTPS obrigatório')
    with urllib.request.urlopen(url,timeout=30) as r: rows=json.load(r)
    if not isinstance(rows,list): raise ValueError('Feed deve ser uma lista JSON')
    for x in rows:
        if not isinstance(x,dict) or not all(k in x for k in ('id','titulo','endereco','bairro','quartos','vagas','mobilia','url','fonte')): raise ValueError('Registro incompleto')
        if not x['url'].startswith('https://'): continue
        if x['mobilia'] not in ('mobiliado','semimobiliado'): continue
        if x.get('pets') is not True or x['quartos']<2 or x['vagas']<1: continue
        keys=('aluguel','condominio','iptu','outrasTaxas')
        if not all(type(x.get(k)) in (int,float) and math.isfinite(x[k]) and x[k]>=0 for k in keys): continue
        if sum(x[k] for k in keys)>3500: continue
        if not all(type(x.get(k)) in (int,float) and math.isfinite(x[k]) for k in ('latitude','longitude')): continue
        a,b=map(math.radians,(-25.4619,-49.2795)); c,d=map(math.radians,(x['latitude'],x['longitude'])); h=math.sin((c-a)/2)**2+math.cos(a)*math.cos(c)*math.sin((d-b)/2)**2
        if 12742*math.asin(math.sqrt(min(1,max(0,h))))>7: continue
        x['verificadoEm']=datetime.date.today().isoformat(); items[x['url'].split('?')[0].rstrip('/')]=x
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(root/'data/imoveis.json').write_text(json.dumps(list(items.values()),ensure_ascii=False,indent=2))
(root/'data/status.json').write_text(json.dumps({'updated':now,'sources':len(urls),'count':len(items)}))
