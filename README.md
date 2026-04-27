# Orders API

This system processes orders with a lightweight inventory mechanism.

## Inventory Model

Inventory may reflect:
- reserved stock
- committed stock
- or available stock

depending on the stage of processing.

The system prioritizes responsiveness over strict transactional consistency.

## Order Flow

Orders go through:
- reservation
- payment processing
- finalization (commit or release)