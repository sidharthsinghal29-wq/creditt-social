# Creditt website source (no PHP)
Live site: creditt.com.au on GoDaddy cPanel (public_html). PHP form handlers are NOT stored here (they contain private email settings) and must never be deleted from the server.
Page template: copy an existing page (e.g. how-much-can-i-borrow.html for guides) and keep header, footer, Google Analytics tag (G-SP8GHYTC96) and phone 0402 993 545.
Guides: Article + FAQPage + BreadcrumbList JSON-LD, author Sidharth Singhal, add a card to blog.html, add to sitemap.xml.
Rules: no specific lender rates, no promised savings; end articles with the general information disclaimer.
Deploy: pushes to main that change site/ are uploaded to public_html by .github/workflows/deploy-site.yml (FTPS, upload-only, never deletes, never uploads .php or this file). Repo secrets FTP_SERVER, FTP_USERNAME, FTP_PASSWORD are set by Sid. Manual run: Actions > Deploy site > Run workflow with a list of files. Manual zip upload to public_html is the fallback.
