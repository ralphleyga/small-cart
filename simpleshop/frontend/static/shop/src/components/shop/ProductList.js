import React, { Component } from 'react'
import ProductSummary from './ProductSummary'

class ProductList extends Component {
    render() {

        const { products } = this.props
        const productList = products ? (
            products.map(product => {
                return (
                    <ProductSummary product={product} key={product.id} />
                )
            })
        ) : (
            <div className="center">No Products</div>
        )


        return (
            <section className='row'>
                {productList}
            </section>
        )
    }
}

export default ProductList