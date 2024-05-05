import React from 'react'

function Navbar(props) {
    return (
        <div>
            <nav class="navbar bg-body-tertiary d-flex align-items-center justify-content-center">
                <div class="container-fluidx">
                    <div class="navbar-brand mb-0 h1">{props.name}</div>
                </div>
            </nav>
        </div>
    )
}

export default Navbar