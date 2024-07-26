<h1>Goals of writing the code:</h1>
<ul>
<li>The purpose of writing this code was to solve the task on PortSwigger: https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses</li>
<li>Uses Blind SQL injection to obtain the password form databases.</li>
</ul>
<h1>Use:</h1>
<ul>
<li>Enter address of your Proxy ( if you have proxy i.e. Burp Suite) or delete this option in line 8 and 20.</li>
<li>Enter URL address in line 20.</li>
<li>Enter value for "session" cookie in line 19 - find it in Dev Tools in your browser.</li>
<li>Enter value for "TrackingId" cookie in line 17 - find it in Dev Tools in your browser. This cookie is vulnerable to a Blind SQL injection attack..</li>
<li>Type in your terminal: <code>python3 blind_sqli.py</code></li>
<li>The password will be different each time.</li>
</ul>
<img width="944" alt="portswigger_blind_sqli_lab" src="https://github.com/user-attachments/assets/d5ce225c-e1c7-4b01-ba89-ac8b429ae85d">

<h1>Author:</h1>
<ul>
<li>Email: <em>ekontakt@wp.pl</em></li>
<li>Linkedin: <a href="https://www.linkedin.com/in/pawel-kubacki-red-team" rel="nofollow">https://www.linkedin.com/in/pawel-kubacki-red-team</a></li>
</ul>
