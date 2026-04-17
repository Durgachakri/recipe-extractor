from recipe_scrapers import scrape_me, scrape_html
from fastapi import HTTPException
from scraper import scrape_recipe

def extract_recipe(url: str):
    try:
        # First try recipe-scrapers directly (fastest)
        try:
            scraper = scrape_me(url)
            return build_response(scraper)
        except Exception as e:
            print(f"Direct scrape failed: {e}, trying manual fetch...")

        # Fallback: manually fetch HTML then parse
        html = scrape_recipe(url)

        if not html:
            raise HTTPException(
                status_code=422,
                detail="Could not fetch the recipe page. The website may be blocking requests."
            )

        scraper = scrape_html(html, org_url=url)
        return build_response(scraper)

    except HTTPException:
        raise  # re-raise HTTP exceptions as-is

    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))


def build_response(scraper) -> dict:
    def safe(fn):
        try:
            result = fn()
            return result if result else None
        except Exception:
            return None

    return {
        "title":        safe(scraper.title),
        "image":        safe(scraper.image),
        "total_time":   safe(scraper.total_time),
        "yields":       safe(scraper.yields),
        "ingredients":  safe(scraper.ingredients),
        "instructions": safe(scraper.instructions),
        "nutrients":    safe(scraper.nutrients),
        "description":  safe(scraper.description),
        "author":       safe(scraper.author),
        "cuisine":      safe(scraper.cuisine),
        "category":     safe(scraper.category),
        "ratings":      safe(scraper.ratings),
        "site_name":    safe(scraper.site_name),
    }