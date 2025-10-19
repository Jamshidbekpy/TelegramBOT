"""Create users table

Revision ID: 715f58abcc31
Revises: 3308905652d2
Create Date: 2025-10-19 18:39:01.462271

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '715f58abcc31'
down_revision: Union[str, Sequence[str], None] = '3308905652d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
