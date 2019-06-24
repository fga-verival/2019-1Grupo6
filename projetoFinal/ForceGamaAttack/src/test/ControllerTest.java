package test;

import static org.hamcrest.CoreMatchers.instanceOf;
import static org.junit.Assert.*;

import java.awt.Window;

import org.junit.Before;
import org.junit.Test;

import controller.Controller;
import jplay.Mouse;

import scenes.spaceShipMenu.SpaceShipMenuScene;

public class ControllerTest {
	private Controller controller;
	
	@Before
	public void setUp() {
		controller = new Controller(); /* Start Game */
	}
	
	
	@Test
	public void testStartGame() {
		assertEquals(controller.update(), true);
	}

	@Test
	public void testQuit() {
		controller.quit();
		assertEquals(controller.update(), false);
	}

	@Test
	public void testPressPause() {
		controller.pressPause();
		assertEquals(controller.getIsPaused(), true);
		controller.pressPause();
		assertEquals(controller.getIsPaused(), false);
		controller.pressPause();
		assertEquals(controller.getIsPaused(), true);
	}
	

	@Test
	public void testGetMouse() {
		Mouse mouse = controller.getMouse();
		System.out.println(mouse);
		equals(mouse == null); /* Mouse começa como nulo. Depois o mouse é instanciado. */
		Mouse mouse2 = new Mouse();
		controller.setMouse(mouse2); /* Setando mouse */
		assertThat(controller.getMouse(), instanceOf(Mouse.class));
	}	

}
