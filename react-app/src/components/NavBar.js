
import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './navbar.css'

const NavBar = () => {

  // slide button functions //
  function openSlide(){
    document.getElementById('slide').style.width = '225px'

  }
  function closeSlide(){
    document.getElementById('slide').style.width = '0px'
  }


  return (
    <nav className='navWrapper'>
      <div id='third'></div>
      <h1 className='navHeader'>Flexmo</h1>
      <div className='sliderWrapper' >
        <button className='sliderButton'
        onClick={() => openSlide()}
        >
          <i
          id='sliderIcon'
          class="fa-solid fa-bars fa-2xl"></i>
        </button>
        <div className='slidePanel' id='slide'>
          <button className='panelClose'
          onClick={() => closeSlide()}
          >
            <i class="fa-regular fa-circle-xmark fa-2xl"></i>
          </button>
          <div className='slideLinks'>
            <NavLink to={'/'}>
              Login
            </NavLink>
            <NavLink to={'/'}>
              Sign up
            </NavLink>
            <NavLink to={'/'}>
              About
            </NavLink>
          </div>
        </div>
        {/* <ul>
          <li>
            <NavLink to='/' exact={true} activeClassName='active'>
              Home
            </NavLink>
          </li>
          <li>
            <NavLink to='/login' exact={true} activeClassName='active'>
              Login
            </NavLink>
          </li>
          <li>
            <NavLink to='/sign-up' exact={true} activeClassName='active'>
              Sign Up
            </NavLink>
          </li>
          <li>
            <NavLink to='/users' exact={true} activeClassName='active'>
              Users
            </NavLink>
          </li>
          <li>
            <LogoutButton />
          </li>
        </ul> */}
      </div>
    </nav>
  );
}

export default NavBar;
