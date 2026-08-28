import zipfile
import os

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portofolio - Teknisi Komputer dan Jaringan</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <nav>
            <h1>Portofolio TKJ</h1>
            <ul>
                <li><a href="#beranda">Beranda</a></li>
                <li><a href="#tentang">Tentang</a></li>
                <li><a href="#keahlian">Keahlian</a></li>
                <li><a href="#proyek">Proyek</a></li>
                <li><a href="#kontak">Kontak</a></li>
            </ul>
        </nav>
    </header>

    <section id="beranda" class="hero">
        <div class="hero-content">
            <h2>Halo, Saya [Nama Anda]</h2>
            <p>Seorang Profesional di Bidang Teknik Komputer dan Jaringan</p>
            <a href="#proyek" class="btn">Lihat Proyek Saya</a>
        </div>
    </section>

    <section id="tentang">
        <h2 class="section-title">Tentang Saya</h2>
        <div class="about-content">
            <div class="about-text">
                <p>Saya adalah individu yang antusias dalam dunia IT, khususnya pada manajemen infrastruktur jaringan dan administrasi server. Latar belakang pendidikan saya di jurusan Teknik Komputer dan Jaringan (TKJ) telah membekali saya dengan pemahaman mendalam secara praktis dan teoretis.</p>
                <p>Ketertarikan saya berfokus pada perancangan jaringan yang efisien serta penanganan masalah <i>troubleshooting</i> dengan cepat dan tepat, guna memastikan konektivitas dan keamanan sistem tetap optimal di berbagai skala lingkungan.</p>
            </div>
        </div>
    </section>

    <section id="keahlian" class="bg-gradient-light">
        <h2 class="section-title">Keahlian & Kompetensi</h2>
        <div class="skills-grid">
            <div class="skill-card">
                <h3>Jaringan Komputer</h3>
                <p>Pemahaman arsitektur LAN, WLAN, dan WAN serta topologi jaringan berbasis standar industri.</p>
            </div>
            <div class="skill-card">
                <h3>Administrasi MikroTik & Cisco</h3>
                <p>Instalasi dan konfigurasi NAT di MikroTik, routing, manajemen bandwidth, serta switching dasar.</p>
            </div>
            <div class="skill-card">
                <h3>Sistem Operasi Server</h3>
                <p>Administrasi server menggunakan Linux (Debian/Ubuntu Server) dan Windows Server.</p>
            </div>
            <div class="skill-card">
                <h3>Hardware & Troubleshooting</h3>
                <p>Perakitan PC, perbaikan masalah hardware & software, serta terminasi kabel fiber dan UTP.</p>
            </div>
        </div>
    </section>

    <section id="proyek">
        <h2 class="section-title">Proyek & Pengalaman</h2>
        <div class="projects-grid">
            <div class="project-card">
                <div class="project-info">
                    <h3>Implementasi MikroTik NAT & Hotspot</h3>
                    <p>Merancang dan mengonfigurasi router MikroTik untuk membagi akses internet ke beberapa <i>client</i> menggunakan metode NAT serta membangun sistem hotspot dengan autentikasi.</p>
                </div>
            </div>
            <div class="project-card">
                <div class="project-info">
                    <h3>Pembangunan Jaringan Lab Komputer</h3>
                    <p>Melakukan instalasi kabel UTP, pengaturan switch, dan konfigurasi IP Address secara statis & DHCP untuk 30 unit komputer klien di laboratorium.</p>
                </div>
            </div>
            <div class="project-card">
                <div class="project-info">
                    <h3>Infrastruktur Sistem Informasi Keuangan</h3>
                    <p>Mengatur infrastruktur server lokal (Web Server Apache, Database MySQL) untuk mendukung kelancaran proses kerja aplikasi sistem keuangan berbasis web.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="kontak">
        <h2 class="section-title">Hubungi Saya</h2>
        <div class="contact-container">
            <p>Tertarik untuk berkolaborasi atau mendiskusikan peluang karir?</p>
            <p>Email: <a href="mailto:emailanda@example.com">emailanda@example.com</a></p>
            <p>LinkedIn: <a href="#">linkedin.com/in/namaanda</a></p>
            <br>
            <a href="mailto:emailanda@example.com" class="btn">Kirim Pesan</a>
        </div>
    </section>

    <footer>
        <p>&copy; 2026 Portofolio TKJ - Dibuat dengan gradasi warna ungu dan putih.</p>
    </footer>
</body>
</html>
"""

css_content = """/* CSS Reset & Variables */
:root {
    --primary-purple: #6a11cb;
    --dark-purple: #4a148c;
    --light-purple: #f3e5f5;
    --accent-purple: #8e24aa;
    --text-dark: #333333;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    scroll-behavior: smooth;
}

body {
    background: linear-gradient(to bottom, var(--light-purple), #ffffff);
    color: var(--text-dark);
    line-height: 1.6;
}

.bg-gradient-light {
    background: linear-gradient(to right, #f3e5f5, #ffffff);
}

/* Navbar */
header {
    background-color: var(--primary-purple);
    color: white;
    padding: 15px 30px;
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 1000;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

nav h1 {
    font-size: 1.5rem;
    letter-spacing: 1px;
}

nav ul {
    list-style: none;
    display: flex;
    gap: 20px;
}

nav ul li a {
    color: white;
    text-decoration: none;
    font-weight: 500;
    transition: 0.3s;
}

nav ul li a:hover {
    color: #d1c4e9;
}

/* Hero Section */
.hero {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    background: linear-gradient(135deg, var(--accent-purple), var(--light-purple), #ffffff);
    padding: 0 20px;
    margin-top: 60px;
}

.hero-content {
    max-width: 800px;
}

.hero-content h2 {
    font-size: 3rem;
    color: var(--dark-purple);
    margin-bottom: 10px;
}

.hero-content p {
    font-size: 1.2rem;
    color: #333;
    margin-bottom: 20px;
}

.btn {
    display: inline-block;
    background: var(--primary-purple);
    color: white;
    padding: 10px 25px;
    text-decoration: none;
    border-radius: 25px;
    font-weight: bold;
    transition: 0.3s;
}

.btn:hover {
    background: var(--dark-purple);
}

/* Section Global */
section {
    padding: 80px 20px;
    max-width: 1100px;
    margin: 0 auto;
}

h2.section-title {
    text-align: center;
    font-size: 2.5rem;
    color: var(--dark-purple);
    margin-bottom: 40px;
    position: relative;
}

h2.section-title::after {
    content: '';
    width: 80px;
    height: 4px;
    background: var(--accent-purple);
    display: block;
    margin: 10px auto 0;
    border-radius: 2px;
}

/* About Section */
.about-content {
    display: flex;
    gap: 40px;
    align-items: center;
}

.about-text {
    flex: 1;
}

.about-text p {
    margin-bottom: 15px;
    font-size: 1.1rem;
}

/* Skills Section */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}

.skill-card {
    background: white;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    text-align: center;
    border-bottom: 4px solid var(--accent-purple);
    transition: transform 0.3s;
}

.skill-card:hover {
    transform: translateY(-5px);
}

.skill-card h3 {
    color: var(--primary-purple);
    margin-bottom: 10px;
}

/* Projects Section */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
}

.project-card {
    background: white;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    border: 1px solid #e1bee7;
}

.project-card .project-info {
    padding: 20px;
}

.project-info h3 {
    color: var(--dark-purple);
    margin-bottom: 10px;
}

/* Contact Section */
.contact-container {
    background: white;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    text-align: center;
}

.contact-container p {
    margin-bottom: 20px;
    font-size: 1.1rem;
}

.contact-container a {
    color: var(--primary-purple);
    font-weight: bold;
    text-decoration: none;
}

/* Footer */
footer {
    background: var(--dark-purple);
    color: white;
    text-align: center;
    padding: 20px;
    margin-top: 40px;
}

/* Responsive */
@media(max-width: 768px) {
    .about-content {
        flex-direction: column;
    }
    nav ul {
        display: none;
    }
}
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

zip_path = "Website-Portofolio-TKJ.zip"
with zipfile.ZipFile(zip_path, 'w') as zipf:
    zipf.write("index.html")
    zipf.write("style.css")

print(f"Created {zip_path}")
