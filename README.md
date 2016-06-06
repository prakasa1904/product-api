<h1>Produc API</h1>
<h5>Author : Prakasa <prakasa@devetek.com></h5>
<h5>Website : http://www.terpusat.com</h5>

<p>Adalah simple API untuk menampilkan data produk, dengan disertai filter. Selain juga menampilkan data kategori yang disusun secara hirarki.</p>
<p>Demo Apps : https://apiproduk.herokuapp.com/</p>
<ul>
<li>Access API Backend : https://apiproduk.herokuapp.com/api-auth/login/
  <ul>
    <li>Username : prakasa</li>
    <li>Password : administrator</li>
  </ul>
</li>
<li>Access UIX CMS Backend : https://apiproduk.herokuapp.com/admin/
  <ul>
    <li>Username : prakasa</li>
    <li>Password : administrator</li>
  </ul>
</li>
</ul>
<p>Unit Test Apps : (Progress)</p>


<h6>:::TEST CASE A JELAS:::</h6>
======================================================================
FAIL: test_details (ver1.tests.ProductTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/prakasa/myPhyton/api/ver1/tests.py", line 16, in test_details
    self.assertEqual(Product.objects.count(), 1)
AssertionError: 0 != 1

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
