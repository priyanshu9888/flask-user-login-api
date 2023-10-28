"""initial database migration

Revision ID: d81055a0454c
Revises: 1c0170eb6b35
Create Date: 2022-07-02 15:35:02.290335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd81055a0454c'
down_revision = '1c0170eb6b35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blacklist_tokens')
    op.drop_column('user', 'registered_on')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('registered_on', sa.DATETIME(), nullable=False))
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('token', sa.VARCHAR(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###
