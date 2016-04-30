py-postmates
============

Hi!

A simple Python client for the Postmates API.

## Setup

You may need to install the secucity pacakge extras for `requests`:

    $ pip install requests[security]

## Usage

Create an instance of the API

```python
import postmates as pm

api = pm.PostmatesAPI(<YOUR_CUSTOMER_ID>, <YOUR_API_KEY>)
```

Create some locations and get a quote for a delivery.

```python
pickup = pm.Location('Alice', '100 Start St, San Francisco, CA', '415-555-0000')
dropoff = pm.Location('Bob', '200 End St, San Francisco, CA', '415-777-9999')

quote = pm.DeliveryQuote(api, pickup.address, dropoff.address)
```

Create a delivery and schedule it.

```python
delivery = Delivery(api, 'a manifest', pickup, dropoff)
delivery.create()
```

Update the status of a pending delivery.

```python
delivery.update_status()
```

If nothing's happened yet, you can cancel (but it will still cost you).

```python
delivery.cancel()
```

Have fun!
