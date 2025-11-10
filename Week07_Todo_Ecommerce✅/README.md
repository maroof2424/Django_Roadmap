

# ✅ **Week 7 Breakdown (Day-by-Day, Full Plan)**

Yeh woh week hai jahan tum **CRUD, relationships, sessions, cart logic, checkout flow** sab crack karoge.
Agar yeh ban gaya → tum ANY Django project handle kar sakte ho.

---

# 🔥 **Day 1 — To-Do App Setup + Models**

**Goals:**

* Project create
* App create
* Model design (Task model)
* Link tasks per-user

**To-Do Model:**

```python
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

✅ Migrate
✅ Test admin

---

# 🔥 **Day 2 — To-Do CRUD (Create + Read)**

* Task list view
* Create task form (POST)
* Only logged-in user ka data dikhana

✅ `login_required` decorator
✅ Show tasks sorted by `completed` status

---

# 🔥 **Day 3 — To-Do Update + Delete + Toggle Status**

* Mark task **Complete / Incomplete**
* Edit title
* Delete task
* Buttons + icons

✅ AJAX optional
✅ Bootstrap UI clean

By end of Day 3 → To-Do App FINISHED ✅

---

# ✅ MINI PROJECT 1 DONE: **To-Do App**

Good job bro.

---

# 🔥 **Day 4 — E-Commerce Setup + Product Model + Product List**

**Models you’ll create:**

```python
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="products/")
```

**Views:**

* Product list page
* Product detail page

✅ Images
✅ Template UI

---

# 🔥 **Day 5 — Cart System (Pure Django Sessions)**

Bro yahan thori dimaag lagay ga
Cart session ke andar chale ga:

**Cart structure example:**

```json
{
    "1": {"quantity": 2},
    "5": {"quantity": 1}
}
```

**Features you’ll build:**
✅ Add to Cart
✅ Remove from Cart
✅ Change quantity
✅ Session save

**Cart summary page**

* Total price calculate
* Item count

---

# 🔥 **Day 6 — Checkout Simulation (No payment, Just Flow)**

Build:

* Checkout page (Name, email, address)
* Order review
* Confirm order page

✅ No real payment → Just simulation
✅ Save "order" in DB

**Order Models (Simple):**

```python
class Order(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

Also:

✅ Clear cart after checkout

---

# 🔥 **Day 7 — Polish + Deploy-Ready Structure**

* Better UI
* Buttons + Alerts (Bootstrap)
* Empty cart handling
* Code cleanup
* Optional: Add product search
* OPTIONAL: Deploy to PythonAnywhere

✅ Week 7 Completed
✅ Django CRUD Master
✅ Session-based Cart Master

---

# ✅ Want FULL CODE?

If you want, I can write:

✅ Full To-Do App (models + views + urls + templates)
✅ Full E-Commerce App (Product list → Cart → Checkout)
✅ With Bootstrap 5 UI
✅ Folder structure
✅ Step-by-step code
