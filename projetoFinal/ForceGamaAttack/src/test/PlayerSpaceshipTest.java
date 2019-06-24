package test;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

import player.Player;
import player.PlayerSpaceship;

public class PlayerSpaceshipTest {
	static String sprite = "src/graphics/img/spaceship.png";
	private PlayerSpaceship playerSpaceship;
	
	@Before
	public void setUp() {
		Player player = new Player(360, 550, sprite);
		playerSpaceship = new PlayerSpaceship(player, 10.5, 12.3, true);
	}
	@Test
	public void testPlayerSpaceship() {
		assertNotNull(playerSpaceship);
	}

	@Test
	public void testGetPlayer() {
		assertNotNull(playerSpaceship.getPlayer());
		assertTrue(playerSpaceship.getPlayer().x == 360);
		assertTrue(playerSpaceship.getPlayer().y == 550);
	}
}
