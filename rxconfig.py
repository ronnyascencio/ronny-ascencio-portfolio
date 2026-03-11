import reflex as rx

config = rx.Config(
    app_name="ronny_ascencio_portfolio",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)