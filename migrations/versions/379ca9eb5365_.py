"""empty message

Revision ID: 379ca9eb5365
Revises: 84f014b38fca
Create Date: 2024-04-16 08:57:21.162029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '379ca9eb5365'
down_revision = '84f014b38fca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
        batch_op.alter_column('restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('pizza_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_constraint('fk_restaurant_pizzas_restaurant_id_restaurants', type_='foreignkey')
        batch_op.drop_constraint('fk_restaurant_pizzas_pizza_id_pizzas', type_='foreignkey')
        batch_op.create_foreign_key(None, 'restaurants', ['restaurant_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'pizzas', ['pizza_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('fk_restaurant_pizzas_pizza_id_pizzas', 'pizzas', ['pizza_id'], ['id'])
        batch_op.create_foreign_key('fk_restaurant_pizzas_restaurant_id_restaurants', 'restaurants', ['restaurant_id'], ['id'])
        batch_op.alter_column('pizza_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
