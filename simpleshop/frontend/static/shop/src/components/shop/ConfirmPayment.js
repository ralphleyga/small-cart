import React, { Component } from 'react'
import { Link } from 'react-router-dom'

class ConfirmPayment extends Component {
    render() {
        return (
            <div className='col-md-12 text-center'>
                <h1>Payment Confirmed</h1>
                <p>You have placed your order.</p>

                <Link className='btn btn-info' to='/products/'>Continue Shopping</Link>
            </div>
        )
    }
}

export default ConfirmPayment