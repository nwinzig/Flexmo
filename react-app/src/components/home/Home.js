import React, {useState, useEffect} from 'react'
import { useParams } from 'react-router-dom'
import './home.css'
function Home(){

    return (
        <div className='homePage'>
            <div className='homeLeft'>
                left
                <h1>Safe, fast, & easy</h1>
                <p>See why a couple people use Flexmo to pay, get paid, and calculate.</p>
                <div className='barcodeHolder'>
                    <p>
                        Scan the code to view a mobile version of my portfolio
                    </p>
                    <div>
                        barcode placeHolder
                    </div>
                </div>
            </div>
            <div className='homeRight'>
                right
                <div>
                    image placeholder
                </div>
            </div>
        </div>
    )
}

export default Home
