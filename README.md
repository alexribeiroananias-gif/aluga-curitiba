# Aluga Curitiba 3.0
Mantém interface 2.2 e catálogo inicial. Não há fonte real conectada. O botão recarrega o catálogo publicado, não consulta portais.
1. Crie repositório GitHub e envie todos os arquivos, inclusive .github/workflows/update.yml.
2. Obtenha um feed JSON autorizado, com lista de registros no formato data/imoveis.json (coordenadas, pets, mobília, todas as taxas mensais, links HTTPS). Outros formatos precisam de adaptador. Não use anúncios de terceiros sem autorização.
3. Em Settings > Secrets and variables > Actions, crie FEED_URLS com um array JSON de URLs HTTPS autorizadas. Não há credenciais de API implementadas.
4. Em Actions, execute Atualizar catálogo manualmente. A rotina substitui o catálogo por registros compatíveis, elimina URLs repetidas e registra a sincronização. Falhas de leitura preservam o catálogo anterior. Agendamento horário sujeito a atrasos do GitHub.
5. No Netlify, conecte o projeto existente ao repositório, sem comando de build, diretório de publicação '.'; cada commit publica o catálogo. Habilite permissões de escrita do workflow se necessário.
Distância em linha reta, referência SEED aproximada herdada da versão anterior. Fotos continuam nos anúncios originais. Não há histórico de preços nem confirmação independente de disponibilidade. A data de sincronização indica importação, não verificação presencial. Não há Supabase nesta versão: JSON versionado reduz configuração.
