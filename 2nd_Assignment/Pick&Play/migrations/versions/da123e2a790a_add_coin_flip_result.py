"""add coin flip result

Revision ID: da123e2a790a
Revises: 
Create Date: 2024-04-26 17:05:02.448832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da123e2a790a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('coin_flip', schema=None) as batch_op:
        batch_op.add_column(sa.Column('result', sa.String(length=10), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('coin_flip', schema=None) as batch_op:
        batch_op.drop_column('result')

    # ### end Alembic commands ###
