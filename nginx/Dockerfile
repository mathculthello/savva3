FROM aeifn/savva3 AS source

FROM nginx
COPY default.conf /etc/nginx/conf.d/default.conf
COPY --from=source /app /app
