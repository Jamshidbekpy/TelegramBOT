"""Create users table

Revision ID: 3308905652d2
Revises: 8c1624de5c24
Create Date: 2025-10-19 18:34:46.062256

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3308905652d2'
down_revision: Union[str, Sequence[str], None] = '8c1624de5c24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
