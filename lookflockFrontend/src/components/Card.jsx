import React from 'react'

function Card(props) {
    return (
        <div className="card m-3 col-lg-3" style={{ width: '18rem' }}>
            <img src={props.imageURL} className="card-img-top" alt="..." />
            <div className="card-body text-start">
                <div>
                    <p className="card-title"><b>{props.name}</b></p>
                </div>
                <div className='d-flex justify-content-between'>
                    <p className="card-text">PKR {props.currentPrice} </p>
                    <p className="card-text" style={{ color: 'red' }}><strike>PKR {props.oldPrice}</strike> </p>
                </div>
                <div>
                    <p className="card-text" style={{ color: 'red' }}> <b>SAVE PKR {props.discount}</b> </p>
                </div>
                <a href="/" className="btn btn-primary">Add To Cart</a>
            </div>
        </div>
    )
}

export default Card