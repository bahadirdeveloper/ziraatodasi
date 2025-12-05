# Security Policy - Silifke Ziraat Odası

## Reporting a Vulnerability

If you discover a security vulnerability within this website, please send an email to bilgi@silifkeziraatodasi.org.tr. All security vulnerabilities will be promptly addressed.

## Security Measures

This website implements the following security measures:

### HTTP Security Headers
- **Strict-Transport-Security (HSTS)**: Forces HTTPS connections
- **Content-Security-Policy (CSP)**: Prevents XSS and injection attacks
- **X-Frame-Options**: Prevents clickjacking
- **X-Content-Type-Options**: Prevents MIME sniffing
- **X-XSS-Protection**: Additional XSS protection
- **Referrer-Policy**: Controls referrer information
- **Permissions-Policy**: Restricts browser features

### Additional Protections
- All external links include `rel="noopener noreferrer"`
- Input sanitization for dynamic content
- URL validation for external links
- No sensitive data stored client-side
- All images served in optimized WebP format
- Static site - no server-side vulnerabilities

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |

## Contact

For security concerns, contact: bilgi@silifkeziraatodasi.org.tr
