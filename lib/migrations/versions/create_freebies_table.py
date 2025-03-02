"""create freebies table

Revision ID: abc123456789

Revises: 5f72c58bf48c

Create Date: 2025-03-01 12:00:00.000000

"""

from alembic import op
import sqlalchemy as sa

revision = 'abc123456789'

down_revision = '5f72c58bf48c'

branch_labbels = None
depends_on = None

def upgrade() -> None:
    op.create_table('freebies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('item_name', sa.String(), nullable=True),
        sa.Column('value', sa.Integer(), nullable=True),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id'), nullable=True),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    def downgrade() -> None:
        op.drop_table('freebies')