"""foreign

Revision ID: e70c81262f6d
Revises: 00dcd5664d53
Create Date: 2021-05-30 22:44:07.520818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e70c81262f6d'
down_revision = '00dcd5664d53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_products_category_id_categories'), 'categories', ['category_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_products_category_id_categories'), type_='foreignkey')
        batch_op.drop_column('category_id')

    # ### end Alembic commands ###