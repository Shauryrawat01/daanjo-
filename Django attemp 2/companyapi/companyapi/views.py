from django.http import HttpResponse


def homepage(request):
    html = """
    <!DOCTYPE html>
    <html lang=\"en\">
    <head>
        <meta charset=\"UTF-8\" />
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
        <title>Company API Home</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 24px; }
            .grid { display: grid; gap: 16px; max-width: 520px; }
            .row { display: flex; gap: 12px; align-items: center; }
            a.btn { display: inline-block; padding: 10px 16px; background:#0d6efd; color:#fff; text-decoration:none; border-radius:6px; }
            a.btn.secondary { background:#198754; }
            input { padding: 10px; border:1px solid #ccc; border-radius:6px; width: 160px; }
            button { padding: 10px 14px; border:0; background:#6c757d; color:#fff; border-radius:6px; cursor:pointer; }
            h1 { margin-top: 0; }
            small { color:#666; }
        </style>
    </head>
    <body>
        <h1>Company API</h1>
        <p>Quick navigation to REST endpoints.</p>
        <div class=\"grid\">
            <div class=\"row\">
                <a class=\"btn\" href=\"/api/companies/\">View Companies</a>
                <a class=\"btn secondary\" href=\"/api/employees/\">View Employees</a>
            </div>
            <div class=\"row\">
                <input id=\"companyId\" type=\"number\" placeholder=\"Company ID\" />
                <button onclick=\"goCompany()\">Go to Company</button>
            </div>
            <div class=\"row\">
                <input id=\"employeeId\" type=\"number\" placeholder=\"Employee ID\" />
                <button onclick=\"goEmployee()\">Go to Employee</button>
            </div>
            <small>Tip: Lists open in the DRF browser. Detail pages require a valid ID that exists in your DB.</small>
        </div>

        <script>
        function goCompany(){
            const id = document.getElementById('companyId').value;
            if(id) window.location.href = '/api/companies/' + id + '/';
        }
        function goEmployee(){
            const id = document.getElementById('employeeId').value;
            if(id) window.location.href = '/api/employees/' + id + '/';
        }
        </script>
    </body>
    </html>
    """
    return HttpResponse(html)