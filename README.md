# Garage Door Referral Site - North Carolina

Static site for a garage door pay-per-call referral service covering North Carolina.

## Structure

- `public/` - the built website. **Set this as the output folder** on Cloudflare Pages or Vercel (no build command needed).
- `build/build.py` - generator. Settings (domain, site name, tracking number) are in `CONFIG` at the top.
- `build/content.py` - all written content (services, guides, FAQs, regional city content).
- `build/style.css`, `build/main.js` - design and scripts.
- `build/data/target-zips.txt` - MarketCall target ZIP list.

## Rebuild

```
pip install zipcodes
python3 build/build.py
```

## Indexing rules (SEO safety)

- Indexed: homepage, NC hub, guides, legal pages, and the cities listed in `TOP_CITIES` in `content.py`.
- All other city pages are `noindex,follow` and left out of `sitemap.xml`.
- To index another city, add it to `TOP_CITIES` with real, specific content, then rebuild.

## Hosting

- Cloudflare Pages: Connect to Git, build command empty, output directory `public`.
- Vercel: Framework "Other", output directory `public`. Note: Vercel Hobby plan does not allow commercial sites.
